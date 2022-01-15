import Plagiarism_detector

assert Plagiarism_detector.shingling_string('I_am_I_am_Sam_the_cat_I_am.', 3) == {'am_', 'm_I', 'e_c', '_I_', 'Sam', 'm_t', '_am', 'm_S', '_th', 'at_', 'am.', 'the', 't_I', '_ca', 'he_', '_Sa', 'I_a', 'cat'}, 'Output was: {}'.format(Plagiarism_detector.shingling_string('I_am_I_am_Sam_the_cat_I_am.', 3))
assert Plagiarism_detector.shingling_string('a rose is a rose is a rose', 3) == {'ar', 'ro', 'ros', 'ose', 'se', 'ei', 'is', 'sa', 'a'}, 'Output was: {}'.format(Plagiarism_detector.shingling_string('a rose is a rose is a rose', 3))
assert Plagiarism_detector.shingling_string('\na\nd  \n\n', 1) == {'', 'a', 'd'}, 'output was: {}'.format(Plagiarism_detector.shingling_string('\na\nd  \n\n', 1))


assert Plagiarism_detector.Jacquards_similarity({'ar', 'ro', 'ros', 'ose', 'se', 'ei', 'is', 'sa', 'a'}, {'ar', 'ro', 'ros', 'ose', 'se', 'ei', 'is', 'sa', 'a'}) == 1.0, 'Output was: {}'.format(Plagiarism_detector.Jacquards_similarity({'ar', 'ro', 'ros', 'ose', 'se', 'ei', 'is', 'sa', 'a'}, {'ar', 'ro', 'ros', 'ose', 'se', 'ei', 'is', 'sa', 'a'}))
assert Plagiarism_detector.Jacquards_similarity({'ard', 'zer', 'yfs', 'fdd'}, {'ar', 'ro', 'ros', 'ose', 'se', 'ei', 'is', 'sa', 'a'}) == 0.0, 'Output was: {}'.format(Plagiarism_detector.Jacquards_similarity({'ard', 'zer', 'yfs', 'fdd'}, {'ar', 'ro', 'ros', 'ose', 'se', 'ei', 'is', 'sa', 'a'})).format({'ard', 'zer', 'yfs', 'fdd'}, {'ar', 'ro', 'ros', 'ose', 'se', 'ei', 'is', 'sa', 'a'})
