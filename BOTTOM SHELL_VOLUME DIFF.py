import trimesh

original = trimesh.load(r"D:\SOFTAGE\2. BOTTOM SHELL\INPUTS\bottom shell.stl")
generated = trimesh.load(r"D:\SOFTAGE\2. BOTTOM SHELL\CODE\BOTTOM SHELL.stl")

print("Original Volume:", original.volume)
print("Generated Volume:", generated.volume)

difference = abs(original.volume - generated.volume)

print("Volume Difference:", difference)
