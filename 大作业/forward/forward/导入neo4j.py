from neo4j import GraphDatabase

def create_graph(tx, line):
    """解析文本行并创建节点和关系"""
    parts = line.strip().split('-')
    start_node = int(parts[0])
    end_node = int(parts[1])
    tx.run("MERGE (n:Node {id: $start_node, name:$start_node_name})",
           start_node=start_node, start_node_name=start_node)
    tx.run("MERGE (m:Node {id: $end_node, name:$end_node_name})",
           end_node=end_node, end_node_name=end_node)
    tx.run("MATCH (n:Node {id: $start_node}), (m:Node {id:$end_node}) "
           "MERGE (n)-[:FORWARDED]->(m)",
           start_node=start_node, end_node=end_node)

def main():
    uri = "bolt://localhost:7687"
    username = ""
    password = ""
    driver = GraphDatabase.driver(uri, auth=(username, password))
    with open("Output1.txt", "r") as f:
        with driver.session() as session:
            for line in f:
                session.write_transaction(create_graph, line)
    driver.close()

if __name__ == "__main__":
    main()
