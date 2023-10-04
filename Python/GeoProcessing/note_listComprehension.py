# List and Dicts
variable_name = [2 * i for i in range(3)] == [0, 2, 4]  # IS THIS POSSIBLE W/CHAINING?
{i: i**2 for i in range(3)} == {0:0, 1:1, 2:4}          # is this correct output? should it be 2:2?

# Scoreandpublish Examples
filterable_cols = [x for x in client_data.columns.tolist() if x not in list(expected_cols.keys())]
physical_risk_rasters = [r for r in os.listdir(physical_risk_rasters_dir) if r.endswith('tif')]
years = list(set([p.split("_")[3].split(".")[0] for p in renamed_list]))
viz_json_dict = [layer["title"] for layer in load(open(webmap_template))["operationalLayers"][1:]]
current_layers = [rl for rl in physical_risk_rasters if rl.split('_')[2]=='baseline'] 
if len([p for p in content_list if p.title == cl_stripped]) == 0:

# Calculate total_risk
calc_cols = ['!'+r.replace('.tif', '')+'!' for r in physical_risk_rasters]
calc_cols = [x for x in calc_cols if ("WindPower" not in x or "Solar" not in x)]
