# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from clustergrammer import Network
import io


def txt2json(input_str="", filename=None):
    net = Network()

    # load matrix file
    # net.load_file('test.txt')
    buff = io.StringIO(input_str)

    if '/' in filename:
        filename = filename.split('/')[-1]

    net.load_tsv_to_net(buff, filename)

    # calculate clustering
    net.make_clust(dist_type='cos', views=['N_row_sum', 'N_row_var'])

    # write visualization json to file
    # net.write_json_to_file('viz', 'mult_view.json')
    json_str_obj = net.export_net_json('viz')

    return json_str_obj


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_f = ""
    with open("test_2.txt", 'r') as f:
        test_f = f.read()

    # The main function.
    # Input: string matrix. Output: string json object.
    json_str_obj = txt2json(test_f, filename='')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
