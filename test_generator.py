import unittest
from lib import word as wd
from lib import separator as sp

class TestWordListUniqueness(unittest.TestCase):

    def setUp(self):
        # Configuration d'un cas de test simple : deux mots avec variantes
        # Mot 1 : "a" avec leet (donnera 'a', '@', '4')
        # Mot 2 : "b" simple
        self.word1 = wd.Word("a")
        self.word1.addLeet() #
        self.word1.loadNumbers() #

        self.word2 = wd.Word("b")
        self.word2.loadNumbers() #

        # Structure globale attendue par Separator
        self.global_tab = [[self.word1], [self.word2]] #

    def test_uniqueness_with_disorder(self):
        """Vérifie que chaque combinaison est unique même avec le mode désordre."""
        my_sep = sp.Separator(self.global_tab) #
        my_sep.addPermutation() #
        my_sep.loadNumbers() #

        total_combinations = my_sep.returnNbCombination() #
        generated_words = []

        for i in range(total_combinations):
            res = my_sep.convertNumberInCombination(i) #
            generated_words.append(res)

        # Utilisation d'un set pour vérifier l'unicité
        # Si la taille du set est égale au nombre de mots générés, il n'y a pas de doublons.
        self.assertEqual(len(generated_words), len(set(generated_words)), 
                         f"Doublons détectés dans les combinaisons ! {generated_words}")

    def test_uniqueness_with_punctuation(self):
        """Vérifie l'unicité avec l'ajout de ponctuation."""
        my_sep = sp.Separator(self.global_tab) #
        my_sep.addCharStarted() #
        my_sep.addCharEnded()   #
        my_sep.loadNumbers()    #

        total_combinations = my_sep.returnNbCombination() #
        results = set()

        for i in range(total_combinations):
            word = my_sep.convertNumberInCombination(i) #
            results.add(word)

        self.assertEqual(len(results), total_combinations, 
                         "Le nombre de résultats uniques ne correspond pas au total prévu.")

if __name__ == '__main__':
    unittest.main()
