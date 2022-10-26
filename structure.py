import os

def make_blank_structure(path, n, name, lec_start, lec_end):
    lname = name.replace(' ', '').lower()
    dname = os.path.join(path, f'{n:02}_{lname}')
    
    if os.path.exists(dname):
        raise ValueError(f'File already exists: {dname}')
    
    os.mkdir(dname)
    
    os.mkdir(os.path.join(dname, 'intro'))
    
    intro_txt = f"# {name}" + "\n\n```{tableofcontents}\n```\n"
    with open(os.path.join(dname, 'intro', 'intro.md'), 'a') as f:
        f.write(intro_txt)
    
    for i in range(lec_start, lec_end + 1):
        lecpath = os.path.join(dname, f'l{i:02}')
        os.mkdir(lecpath)
        os.mkdir(os.path.join(lecpath, 'figures'))
        
        lec_txt = f"(lecture_{i:02})=\n# Lecture {i:02}"
        
        with open(os.path.join(lecpath, f'l{i:02}.md'), 'a') as f:
            f.write(lec_txt)
            
if __name__ == '__main__':
    make_blank_structure('./book', 0, 'Intro', 1, 3)
    make_blank_structure('./book', 1, 'Groundwater', 4, 7)
    make_blank_structure('./book', 2, 'Cryosphere', 8, 12)
    make_blank_structure('./book', 3, 'Rivers', 13, 18)
    make_blank_structure('./book', 4, 'Atmosphere', 19, 24)
    make_blank_structure('./book', 5, 'Global Environment', 26, 34)
    make_blank_structure('./book', 6, 'Ocean Carbon', 35, 39)
    make_blank_structure('./book', 7, 'Land Biosphere', 40, 43)
    make_blank_structure('./book', 8, 'Polar Case Study', 44, 45)
    make_blank_structure('./book', 9, 'Global Climate', 46, 48)
    make_blank_structure('./book', 10, 'Energy Transitions', 49, 57)
    
    