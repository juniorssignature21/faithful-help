import re

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define old and new pricing content patterns
old_basic = '''<h1>Professional</h1>
                                                <p>Ut enim ad minim veniam, quis istomw nostrud exercitation ullamco laboris nisi ut aliquip ex ea
                                                    commodo.</p>
                                                <a data-animation="fadeInLeft" data-delay=".6s" href="#" class="btn btn-icon ml-0"><span>+</span>Price:
                                                    $489.00</a>'''

new_basic = '''<h1>Basic Home Care</h1>
                                                <p>Daytime companion care and basic assistance with daily activities for clients requiring part-time support.</p>
                                                <a data-animation="fadeInLeft" data-delay=".6s" href="#" class="btn btn-icon ml-0"><span>+</span>Contact Us</a>'''

old_advanced = '''<h1>Advanced</h1>
                                                <p>Ut enim ad minim veniam, quis istomw nostrud exercitation ullamco laboris nisi ut aliquip ex ea
                                                    commodo.</p>
                                                <a data-animation="fadeInLeft" data-delay=".6s" href="#" class="btn btn-icon ml-0"><span>+</span>Price:
                                                    $489.00</a>'''

new_advanced = '''<h1>24/7 Full Care</h1>
                                                <p>Round-the-clock professional caregiving with overnight support for clients with complex care needs.</p>
                                                <a data-animation="fadeInLeft" data-delay=".6s" href="#" class="btn btn-icon ml-0"><span>+</span>Contact Us</a>'''

old_advantage = '''<h1>Advantage</h1>
                                                <p>Ut enim ad minim veniam, quis istomw nostrud exercitation ullamco laboris nisi ut aliquip ex ea
                                                    commodo.</p>
                                                <a data-animation="fadeInLeft" data-delay=".6s" href="#" class="btn btn-icon ml-0"><span>+</span>Price:
                                                    $489.00</a>'''

new_advantage = '''<h1>Hospital Support</h1>
                                                <p>Professional in-hospital caregiving ensuring patient comfort and continuous attention during hospital stays.</p>
                                                <a data-animation="fadeInLeft" data-delay=".6s" href="#" class="btn btn-icon ml-0"><span>+</span>Contact Us</a>'''

# Replace all instances
content = content.replace(old_basic, new_basic)
content = content.replace(old_advanced, new_advanced)
content = content.replace(old_advantage, new_advantage)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Pricing boxes updated successfully")
