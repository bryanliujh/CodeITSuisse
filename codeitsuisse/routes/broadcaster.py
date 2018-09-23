import logging
import json

from flask import request, jsonify

from codeitsuisse import app;
from codeitsuisse.routes.graph import Graph
from codeitsuisse.routes.graph import shortest_path

logger = logging.getLogger(__name__)


@app.route('/broadcaster/most-connected-node', methods=['POST'])
def broadcaster_most_connected():
    graph_dic = {}
    data = request.get_json()

    for item in data["data"]:
        i_arr = item.split(",")
        # time_dic[i_arr[0]] = i_arr[1]
        # time_arr.append(i_arr[1])
        j = i_arr[0].split("->")
        if j[0] in graph_dic:
            graph_dic[j[0]].append(j[1])
        else:
            graph_dic[j[0]] = [j[1]]

    logging.info(graph_dic)

    def max_length(x):
        return len(graph_dic[x])

    # Determine what index has the longest value
    index = max(graph_dic, key=max_length)
    m = len(graph_dic[index])

    # Fill the list with `m` zeroes
    out = [0 for x in range(m + 1)]

    for k in graph_dic:
        l = len(graph_dic[k])
        out[l] += 1
    logging.info(out)
    return "hi"


@app.route('/broadcaster/fastest-path', methods=['POST'])
def broadcaster_fastest_path():
    data = request.get_json()

    graph = Graph()
    graph_dic = {}
    node_arr = []
    time_dic = {}
    time_arr = []
    set_node_arr = []

    sender = data["sender"]
    recipient = data["recipient"]

    for item in data["data"]:
        i_arr = item.split(",")
        #time_dic[i_arr[0]] = i_arr[1]
        #time_arr.append(i_arr[1])
        j = i_arr[0].split("->")
        if j[0] in graph_dic:
            graph_dic[j[0]].append(j[1]+';'+i_arr[1])
        else:
            graph_dic[j[0]] = [j[1]+';'+i_arr[1]]


        node_arr.append(j[0])
        node_arr.append(j[1])
        set_node_arr = sorted(set(node_arr))

    logging.info(time_dic)
    logging.info(graph_dic)
    logging.info(set_node_arr)


    for node in set_node_arr:
        graph.add_node(node)
    for edge_key, edge_value in graph_dic.items():
        for edge in edge_value:
            e = edge.split(';')
            logging.info(edge_key)
            graph.add_edge(edge_key, e[0], e[1])



    #shortest_path(graph, sender, recipient)
    #logging.info(shortest_path(graph, sender, recipient))

    return jsonify(time_dic)



