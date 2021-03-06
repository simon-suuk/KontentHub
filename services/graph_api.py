import requests


class PageOrPost:
    def __init__(self, page_id, page_token):
        self.node_id = page_id
        self.access_token = page_token

    def get_edge(self, edge_name):
        """
        To read an edge, you must include both the node ID and the edge name in the path.
        For example, /page nodes have a /feed edge which
        can return all Post nodes on a Page

        :param edge_name:
        """
        base_url = "https://graph.facebook.com"
        version = "v2.12"
        url = "{base_url}/{version}/{node_id}/{edge_name}?access_token={access_token}".format(
            base_url=base_url,
            version=version,
            node_id=self.node_id,
            edge_name=edge_name,
            access_token=self.access_token
        )
        response = requests.get(url)
        return response.json()

    def get_node_properties(self, *args):
        """
        Fields are node properties.
        The Page node reference indicates which fields
        you can ask for when reading a Page node.
        For example, If you wanted to get the about, fan_count, and website fields

        :param args:
        """
        base_url = "https://graph.facebook.com"
        version = "v2.12"
        url = "{base_url}/{version}/{node_id}?fields={fields}&access_token={access_token}".format(
            base_url=base_url,
            version=version,
            node_id=self.node_id,
            fields="%2C".join([arg for arg in args]),
            access_token=self.access_token
        )
        response = requests.get(url)
        # print("type: {}".format(type(response.json())))
        return response.json()

    def get_node_edge_properties(self, metric):
        """
        Fields are node properties.
        The Page node reference indicates which fields
        you can ask for when reading a Page node.
        For example, If you wanted to get the about, fan_count, and website fields

        :param metric:
        :param edge_name:
        :param args:
        """
        # "https://graph.facebook.com/v2.12/1420595431516143_1458058417769844/insights/post_impressions_unique?lifetime&access_token=EAA"
        base_url = "https://graph.facebook.com"
        version = "v2.12"
        url = "{base_url}/{version}/{node_id}/insights/{metric}?lifetime&access_token={access_token}".format(
            base_url=base_url,
            version=version,
            node_id=self.node_id,
            metric=metric,
            access_token=self.access_token
        )
        response = requests.get(url)
        # print("type: {}".format(type(response.json())))
        return response.json()
