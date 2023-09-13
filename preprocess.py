import os
import nbformat
def filter_code_files(repo):
    code_file_extensions=['.py','.js','.c','.cpp','.java','.html','.css','.rb']
    code_files=[file for file in repo if os.path.splitext(file)[1] in code_file_extensions]
    return code_files
def extract_code_from_notebook(notebook_content):
    nb=nbformat.reads(notebook_content,as_version=4)
    code_cells=[cell['source'] for cell in nb.cells if cell.cell_type=='code']
    return "\n".join(code_cells)
