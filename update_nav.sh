#!/bin/bash

# Update navigation across all HTML files
for file in *.html; do
  # Remove old menu structure and replace with new one
  sed -i '/<nav id="mobile-menu">/,/<\/nav>/c\
                            <nav id="mobile-menu">\
                                <ul>\
                                    <li><a href="index.html">Home</a></li>\
                                    <li><a href="about.html">About Us</a></li>\
                                    <li><a href="services.html">Services +</a>\
                                        <ul class="submenu">\
                                            <li><a href="services.html">Home-Based Elderly Care</a></li>\
                                            <li><a href="services-2.html">Hospital Support Care</a></li>\
                                            <li><a href="services-details.html">Caregiver Training</a></li>\
                                            <li><a href="service-details.html">Free Medical Outreach</a></li>\
                                        </ul>\
                                    </li>\
                                    <li><a href="doctor.html">Our Team</a></li>\
                                    <li><a href="blog.html">Resources +</a>\
                                        <ul class="submenu">\
                                            <li><a href="blog.html">Healthcare Tips</a></li>\
                                            <li><a href="blog-2-col.html">Caregiver Guide</a></li>\
                                            <li><a href="blog-details.html">Success Stories</a></li>\
                                        </ul>\
                                    </li>\
                                    <li><a href="contact.html">Contact</a></li>\
                                    <li><a href="{% url "core:book-appointment" %}" class="special-btn">Schedule Consultation</a></li>\
                                </ul>\
                            </nav>' "$file"
done

echo "Navigation menus updated successfully"
