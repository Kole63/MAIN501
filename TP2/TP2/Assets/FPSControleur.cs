using UnityEngine;
using UnityEngine.InputSystem;

[RequireComponent(typeof(CharacterController))]
public class FPSControleur : MonoBehaviour
{
    [Header("References")]
    [SerializeField] private Transform cameraTransform;

    [Header("Mouvement")]
    [SerializeField] private float vitesseDeplacement = 5f;
    [SerializeField] private float multiplicateurSprint = 5f;
    [SerializeField] private float hauteurSaut = 1.2f;
    [SerializeField] private float gravite = -9.81f;

    [Header("Regard")]
    [SerializeField] private float sensibiliteSouris = 0.1f;
    [SerializeField] private float angleRegardMax = 80f;

    private CharacterController controleur;

    private Vector2 entreeDeplacement;
    private Vector2 entreeRegard;
    private bool sprintActif;
    private float vitesseVerticale;
    private float tangage;

    private InputAction actionDeplacement;
    private InputAction actionRegard;
    private InputAction actionSaut;
    private InputAction actionSprint;

    private void Awake()
    {
        controleur = GetComponent<CharacterController>();

        if (cameraTransform == null)
        {
            Camera cam = GetComponentInChildren<Camera>();
            if (cam != null)
                cameraTransform = cam.transform;
        }

        actionDeplacement = new InputAction("Deplacement", InputActionType.Value);
        actionDeplacement.AddCompositeBinding("2DVector")
            .With("Up", "<Keyboard>/w")
            .With("Down", "<Keyboard>/s")
            .With("Left", "<Keyboard>/a")
            .With("Right", "<Keyboard>/d");

        actionRegard = new InputAction("Regard", InputActionType.Value, "<Mouse>/delta");
        actionSaut = new InputAction("Saut", InputActionType.Button, "<Keyboard>/space");
        actionSprint = new InputAction("Sprint", InputActionType.Button);
        actionSprint.AddBinding("<Keyboard>/leftShift");
        actionSprint.AddBinding("<Keyboard>/rightShift");
    }

    private void OnEnable()
    {
        actionDeplacement.Enable();
        actionRegard.Enable();
        actionSaut.Enable();
        actionSprint.Enable();

        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
    }

    private void OnDisable()
    {
        actionDeplacement.Disable();
        actionRegard.Disable();
        actionSaut.Disable();
        actionSprint.Disable();

        Cursor.lockState = CursorLockMode.None;
        Cursor.visible = true;
    }

    private void Update()
    {
        LireEntrees();
        GererRegard();
        GererDeplacement();
    }

    private void LireEntrees()
    {
        entreeDeplacement = actionDeplacement.ReadValue<Vector2>();
        entreeRegard = actionRegard.ReadValue<Vector2>();
        sprintActif = actionSprint.IsPressed();
    }

    private void GererRegard()
    {
        float sourisX = entreeRegard.x * sensibiliteSouris;
        float sourisY = entreeRegard.y * sensibiliteSouris;

        tangage -= sourisY;
        tangage = Mathf.Clamp(tangage, -angleRegardMax, angleRegardMax);

        transform.Rotate(Vector3.up * sourisX);

        if (cameraTransform != null)
            cameraTransform.localRotation = Quaternion.Euler(tangage, 0f, 0f);
    }

    private void GererDeplacement()
    {
        if (controleur.isGrounded && vitesseVerticale < 0f)
            vitesseVerticale = -2f;

        if (actionSaut.triggered && controleur.isGrounded)
            vitesseVerticale = Mathf.Sqrt(hauteurSaut * -2f * gravite);

        vitesseVerticale += gravite * Time.deltaTime;

        float vitesseActuelle = sprintActif ? vitesseDeplacement * multiplicateurSprint : vitesseDeplacement;
        Vector3 horizontal = (transform.right * entreeDeplacement.x + transform.forward * entreeDeplacement.y) * vitesseActuelle;
        Vector3 mouvement = horizontal + Vector3.up * vitesseVerticale;
        controleur.Move(mouvement * Time.deltaTime);
    }
}
