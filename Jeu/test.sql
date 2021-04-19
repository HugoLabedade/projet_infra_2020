--EXO 1
SELECT l.titre, a.nom, a.prenom
FROM Livres l
INNER JOIN Auteurs a ON (l.id_auteur=a.id_auteur)

--EXO 2
SELECT e.nom, e.prenom, ee.date_pret, ee.date_rendu
FROM Emprunteur e
INNER JOIN Emprunts ee ON (e.id_emprunteur=ee.id_emprunteur)

--EXO 3
SELECT l.titre, CONCAT(a.nom,' ', a.prenom), e.nom
FROM Livres l
INNER JOIN Auteurs a ON (l.id_auteur=a.id_auteur)
INNER JOIN Emprunts ee ON (l.id_livre=ee.id_livre)
INNER JOIN Emprunteur e ON (ee.id_emprunteur=e.id_emprunteur)

--EXO 4
SELECT ee.id_emprunt, e.nom 
FROM Emprunts ee 
INNER JOIN Emprunteur ee ON (ee.id_emprunteur=e.id_emprunteur)

--EXO 5
SELECT ee.id_emprunt, e.nom 
FROM Emprunts ee 
INNER JOIN Emprunteur e ON (ee.id_emprunteur=e.id_emprunteur)
WHERE e.id_emprunteur IS NOT NULL

--EXO 6
SELECT ee.id_emprunt 
FROM Emprunts ee 
INNER JOIN Emprunteur e ON (ee.id_emprunteur=e.id_emprunteur)
WHERE e.id_emprunteur IS NULL

