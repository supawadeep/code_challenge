import unittest
from src.find_shortest import *

class TestShortest(unittest.TestCase):

    def test_data(self):
        file_name = "graph.csv"
        list_node = [["A","B"],["B","A"],["C","F"],["F","G"],["F","C"],["A","I"],["H","H"],["E","C"]]
        final_res = []
        for (start, end) in list_node:
            file = read_file(file_name)
            res_data = find_shortest_path(file, start, end)
            final_res.append(result_(res_data,start, end))
            
        self.assertEqual(final_res[0], "Path from A to B is A -> B, and have cost 5")
        self.assertEqual(final_res[1], "Path from B to A is B -> A, and have cost 5")
        self.assertEqual(final_res[2], "Path from C to F is C -> G -> H -> F, and have cost 10")
        self.assertEqual(final_res[3], "Path from F to G is F -> H -> G, and have cost 8")
        self.assertEqual(final_res[4], "Path from F to C is F -> H -> G -> C, and have cost 10")
        self.assertEqual(final_res[5], "Path is not reachable")
        self.assertEqual(final_res[6], "Path from H to H is H, and have cost 0")
        self.assertEqual(final_res[7], "Path from E to C is E -> A -> B -> C, and have cost 13")


if __name__ == '__main__':
    unittest.main()
