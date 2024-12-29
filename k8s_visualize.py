import dash
from dash import html, dcc, Input, Output
import dash_cytoscape as cyto
from kubernetes import client, config

# Fetch Kubernetes cluster data
def fetch_k8s_cluster_data():
    config.load_kube_config()
    v1 = client.CoreV1Api()

    nodes = v1.list_node().items
    pods = v1.list_pod_for_all_namespaces().items
    services = v1.list_service_for_all_namespaces().items

    cluster_data = {
        "nodes": [node.metadata.name for node in nodes],
        "pods": [(pod.metadata.name, pod.spec.node_name) for pod in pods],
        "services": [service.metadata.name for service in services],
    }
    return cluster_data

# Create Cytoscape elements
def create_elements(data):
    elements = []
    # Add nodes
    for node in data['nodes']:
        elements.append({"data": {"id": node, "label": node, "type": "Node"}, "classes": "node"})
    for pod, node in data['pods']:
        elements.append({"data": {"id": pod, "label": pod, "type": "Pod"}, "classes": "pod"})
        elements.append({"data": {"source": node, "target": pod}})
    for service in data['services']:
        elements.append({"data": {"id": service, "label": service, "type": "Service"}, "classes": "service"})
        for pod, _ in data['pods']:
            elements.append({"data": {"source": service, "target": pod}})
    return elements

# Define Dash app
app = dash.Dash(__name__)
app.title = "Kubernetes Cluster Visualization"

# Load data
cluster_data = fetch_k8s_cluster_data()
elements = create_elements(cluster_data)

# App layout
app.layout = html.Div([
    html.H1("Kubernetes Cluster Visualization", style={'textAlign': 'center'}),
    html.Div([
        html.Label("Select Layout:"),
        dcc.Dropdown(
            id='layout-dropdown',
            options=[
                {'label': 'Grid', 'value': 'grid'},
                {'label': 'Circle', 'value': 'circle'},
                {'label': 'Breadthfirst', 'value': 'breadthfirst'},
                {'label': 'Random', 'value': 'random'}
            ],
            value='circle',
            style={'width': '200px'}
        )
    ], style={'marginBottom': '10px'}),
    cyto.Cytoscape(
        id='k8s-graph',
        elements=elements,
        style={'width': '100%', 'height': '600px'},
        layout={'name': 'circle'},
        stylesheet=[
            {'selector': '.node', 'style': {'background-color': 'blue', 'label': 'data(label)'}},
            {'selector': '.pod', 'style': {'background-color': 'green', 'label': 'data(label)'}},
            {'selector': '.service', 'style': {'background-color': 'red', 'label': 'data(label)'}},
            {'selector': 'edge', 'style': {'line-color': 'gray'}}
        ]
    ),
    html.Div(id='node-data', style={'marginTop': '20px', 'textAlign': 'center'})
])

# Callbacks for interactivity
@app.callback(
    Output('k8s-graph', 'layout'),
    Input('layout-dropdown', 'value')
)
def update_layout(layout):
    return {'name': layout}

@app.callback(
    Output('node-data', 'children'),
    Input('k8s-graph', 'tapNodeData')
)
def display_node_data(data):
    if data:
        return html.Div([
            html.H4("Node Details"),
            html.P(f"ID: {data['id']}"),
            html.P(f"Type: {data['type']}")
        ])
    return html.Div("Click on a node to see details")

# Run the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)

# import dash
# from dash import html
# import dash_cytoscape as cyto
# from kubernetes import client, config


# # def fetch_k8s_cluster_data():
# #     config.load_kube_config()
# #     v1 = client.CoreV1Api()

# #     nodes = v1.list_node().items
# #     pods = v1.list_pod_for_all_namespaces().items
# #     services = v1.list_service_for_all_namespaces().items

# #     cluster_data = {
# #         "nodes": [node.metadata.name for node in nodes],
# #         "pods": [(pod.metadata.name, pod.spec.node_name) for pod in pods],
# #         "services": [service.metadata.name for service in services],
# #     }
# #     return cluster_data

# # def create_elements(data):
# #     elements = []
# #     # Add nodes
# #     for node in data['nodes']:
# #         elements.append({"data": {"id": node, "label": node}, "classes": "node"})
# #     for pod, node in data['pods']:
# #         elements.append({"data": {"id": pod, "label": pod}, "classes": "pod"})
# #         elements.append({"data": {"source": node, "target": pod}})
# #     for service in data['services']:
# #         elements.append({"data": {"id": service, "label": service}, "classes": "service"})
# #         for pod, _ in data['pods']:
# #             elements.append({"data": {"source": service, "target": pod}})
# #     return elements

# # def run_dash_app(elements):
# #     app = dash.Dash(__name__)

# #     app.layout = html.Div([
# #         cyto.Cytoscape(
# #             id='k8s-graph',
# #             elements=elements,
# #             style={'width': '100%', 'height': '800px'},
# #             layout={'name': 'circle'},
# #             stylesheet=[
# #                 {'selector': '.node', 'style': {'background-color': 'blue', 'label': 'data(label)'}},
# #                 {'selector': '.pod', 'style': {'background-color': 'green', 'label': 'data(label)'}},
# #                 {'selector': '.service', 'style': {'background-color': 'red', 'label': 'data(label)'}},
# #                 {'selector': 'edge', 'style': {'line-color': 'gray'}}
# #             ]
# #         )
# #     ])

# #     app.run_server(debug=True)

# # if __name__ == "__main__":
# #     cluster_data = fetch_k8s_cluster_data()
# #     elements = create_elements(cluster_data)
# #     run_dash_app(elements)
