def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="content">
    <h4 class="title">
        ''' + concept_title
    html_text_2 = '''
    </h4>
    <p class="paragraph">
        ''' + concept_description
    html_text_3 = '''
    </p>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        concept = text[next_concept_start:next_concept_end]
        text = text[next_concept_end:]
    return concept

NOTES = """TITLE: Functions Within Python
DESCRIPTION: Also known as procedures, functions take given input, does a specified job to that input, and then gives output. They work by Input-> Function-> Output. Once you have written a function once, you never have to program it again. This allows for programmers to avoid repitition. Using inputs within the procedures, equations can be programmed to work when printed. If the equation doesn't have a return statement, then the ouput will be 'none'.
TITLE: If and While
DESCRIPTION: 'If' executes when the test expression is true. This is a helpful tool when writing expressions that you may only want to execute under certain conditions. If the conditions you programmed are correct, then the 'if' statement will compute. While executes as long as the test expression is true. While can be used to have a test expression compute itself inefinetely, or at least until you program it to stop. A break test is another helpful tool within Python programming. If you insert a break test within a 'while' loop, the expression will keep executing the while statement until the break test is 'True'. But as long as the break test is false, the while expression will continue looping.
TITLE: List Operations
DESCRIPTION: Lists have a few helpful operations that allow for more flexibility within their programming. Two of the operations are very similar, .append and concatenations. The difference exists in what they produce as an outcome. Where .append adds an element to an already existing list (it mutates the old list), concatenating puts two lists together into a new list."""
        
def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html


print generate_all_html(NOTES)