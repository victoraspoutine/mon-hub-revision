import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Révisions Éco", page_icon="🎓", layout="centered")

# CSS pour rendre les cartes jolies
st.markdown("""
<style>
    .flashcard {
        background-color: #f0f2f6;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        min-height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .question { font-size: 24px; font-weight: bold; color: #333; }
    .reponse { font-size: 20px; color: #0068c9; margin-top: 20px; border-top: 2px solid #ddd; padding-top: 15px;}
</style>
""", unsafe_allow_html=True)

# Barre latérale
menu = st.sidebar.radio("Matières", ["📈 Analyse Économique", "📜 Histoire Économique"])

# --- SECTION 1 : ANALYSE ÉCO (Flashcards TD 6-7) ---
if menu == "📈 Analyse Économique":
    st.title("📈 TD 6-7 : Entraînement")

    # --- C'EST ICI QUE TU MODIFIES TES QUESTIONS/RÉPONSES ---
    # J'ai mis des exemples classiques de TD 6-7 (Coûts et Marchés)
    # Remplace le texte entre les guillemets "" par tes vrais exos.
    flashcards = [
        {
            "question": "TD6 - Qu'est-ce que le Coût Marginal (Cm) ?",
            "reponse": "C'est le coût de production d'une unité supplémentaire. Mathématiquement : Cm = Dérivée du Coût Total (CT')."
        },
        {
            "question": "TD6 - Condition de maximisation du profit en CPP ?",
            "reponse": "Le profit est maximal quand le Prix (P) est égal au Coût Marginal (Cm). Donc P = Cm."
        },
        {
            "question": "TD7 - Définition du Monopole",
            "reponse": "Structure de marché où il n'y a qu'un seul offreur face à une multitude de demandeurs. Le faiseur de prix (Price maker)."
        },
        {
            "question": "TD7 - L'indice de Lerner (Pouvoir de marché)",
            "reponse": "L = (P - Cm) / P. Plus L est proche de 1, plus le pouvoir de monopole est fort."
        },
        {
            "question": "TD7 - Différence entre CPP et Monopole sur le surplus ?",
            "reponse": "Le monopole réduit le surplus du consommateur et crée une 'perte sèche' pour la société par rapport à la CPP."
        }
    ]
    # ---------------------------------------------------------

    # Gestion de l'état (pour savoir à quelle carte on est)
    if 'card_index' not in st.session_state:
        st.session_state.card_index = 0
    if 'show_answer' not in st.session_state:
        st.session_state.show_answer = False

    # Récupérer la carte actuelle
    current_card = flashcards[st.session_state.card_index]

    # Affichage de la barre de progression
    st.progress((st.session_state.card_index + 1) / len(flashcards))
    st.caption(f"Carte {st.session_state.card_index + 1} sur {len(flashcards)}")

    # Affichage de la carte
    reponse_html = f"<div class='reponse'>{current_card['reponse']}</div>" if st.session_state.show_answer else ""
    
    st.markdown(f"""
    <div class="flashcard">
        <div class="question">{current_card['question']}</div>
        {reponse_html}
    </div>
    """, unsafe_allow_html=True)

    # Boutons de contrôle
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("⬅️ Précédent"):
            if st.session_state.card_index > 0:
                st.session_state.card_index -= 1
                st.session_state.show_answer = False
                st.rerun()

    with col2:
        if st.button("👀 Révéler / Cacher la réponse", use_container_width=True):
            st.session_state.show_answer = not st.session_state.show_answer
            st.rerun()

    with col3:
        if st.button("Suivant ➡️"):
            if st.session_state.card_index < len(flashcards) - 1:
                st.session_state.card_index += 1
                st.session_state.show_answer = False
                st.rerun()

# --- SECTION 2 : HISTOIRE ÉCO ---
elif menu == "📜 Histoire Économique":
    st.title("📜 Histoire Économique")
    st.info("Espace dédié aux notes de cours et frises chronologiques.")
    
    # Zone de prise de notes simple pour l'instant
    st.subheader("Mes Fiches de révision")
    
    sujet = st.text_input("Sujet (ex: Révolution Industrielle)")
    contenu = st.text_area("Contenu clé à retenir", height=200)
    
    if st.button("Sauvegarder la note"):
        st.success(f"Note sur '{sujet}' enregistrée (simulation) !")
