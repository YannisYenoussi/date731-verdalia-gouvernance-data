# Checklist de rendu

À cocher par le groupe. Aucune case n'est cochée d'avance.

## Contenu
- [ ] Les neuf parties officielles du cahier des charges sont présentes (confrontation faite)
- [ ] Les dix exigences sont traitées (`docs/09-matrice-tracabilite.md`)
- [ ] Hypothèses identifiées (`docs/sources/HYPOTHESES_QUESTIONS.md`)
- [ ] Durées de conservation qualifiées (obligation, recommandation, proposition)
- [ ] Sources juridiques relues sur les sites officiels
- [ ] IAgraphie complétée et signée
- [ ] Noms des trois membres sur la page de garde

## Diagrammes
- [ ] Les huit diagrammes sont cohérents avec le texte
- [ ] Exports régénérés : `bash scripts/build_diagrams.sh`

## Livrables
- [ ] Dossier Word régénéré et ouvert : `python3 scripts/build_docx.py`
- [ ] PowerPoint régénéré et ouvert : `python3 scripts/build_pptx.py`
- [ ] Durée de la présentation chronométrée à 15 minutes
- [ ] Parole équitable entre les trois orateurs
- [ ] Liens internes vérifiés : `python3 scripts/check_links.py`

## Git
- [ ] Branches fusionnées dans `main` après relecture
- [ ] Aucun fichier temporaire commité
- [ ] README à jour (section état d'avancement)
