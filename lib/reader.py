
def matches_found(result) -> bool:
    """Parses lookup results to determine if matches found."""
    if isinstance(result[0], dict):
        return True
    else:
        return False 

def returned_similar_words(result) -> bool:
    """Parses lookup results to determine if similar words returned."""
    if isinstance(result[0], str):
        return True 
    else:
        return False 

def get_pos(d:dict) -> str:
    try:
        return d['fl']
    except:
        return ''
    
def get_pronunciations(d:dict) -> str:
    pronunciations = d.get('hwi')
    hw = pronunciations.get('hw')
    try:
        mw = pronunciations['prs'][0]['mw']
        mw = [p.get('mw') for p in pronunciations['prs']]
        mw = '; '.join(mw)
        return f'{hw} | {mw}'
    except:
        return hw

def get_shortdef(d:dict) -> str:
    return d['shortdef'][0]