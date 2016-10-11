import str_gadgets
import unittest, json, logging, os

class ChunkerGoodInput(unittest.TestCase):
    def test_good_inputs(self):
        ''' testing chunker with known good input-output pairs '''

        # Open the file with test data (known good input-output)
        oracle_file_name = 'oracles.json'
        if os.path.exists(oracle_file_name):
           f = open(oracle_file_name, "r")
           oracles = json.load(f)
           f.close()
        else:
            logging.error("Input-output file %s not found." %oracle_file_name)
            return 0

		# feeding input strings and length of chunks into str_gadgets.chunker()
		#+and asserting that the returned lists are the same as in oracles.json
        for inp_str, n, output_list in oracles:
            chunks = str_gadgets.chunker(inp_str, n)
            self.assertEqual(chunks, output_list)

        # (optional) Dump g_i as JSON file into working directory
        # f = open("g_i.json", "w")
        # json.dump(g_i, f)
        # f.close()
        
        return 1

if __name__ == '__main__':
    unittest.main()