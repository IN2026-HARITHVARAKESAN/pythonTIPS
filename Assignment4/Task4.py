"""This file contains json_analyzer() which flattens a JSON object and counts the number of keys at each depth."""

import json


def json_analyzer(filename: str) -> dict:
	"""Flatten JSON object and count keys at each depth."""
	with open(filename, "r") as file:
		data = json.load(file)

	flattened_json = {}
	key_count_by_depth = {}

	def visit_depth(value, path="", depth=0):
		if isinstance(value, dict):
			key_count_by_depth[depth] = len(value) + key_count_by_depth.get(depth, 0)
			for key, child in value.items():
				if path:
					child_path = f"{path}_{key}"
				else:
					child_path = key
				visit_depth(child, child_path, depth + 1)
		else:
			flattened_json[path] = value

	visit_depth(data)

	return {
		"flattened": flattened_json,
		"key_count_by_depth": key_count_by_depth,
	}

if __name__ == "__main__":
	filename = input("Enter the JSON filename and path: ")
	result = json_analyzer(filename)
	print(f"Flattened JSON: {result['flattened']}")
	print(f"Key count by depth: {result['key_count_by_depth']}")