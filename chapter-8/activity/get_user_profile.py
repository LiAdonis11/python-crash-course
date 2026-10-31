import user_profile
from user_profile import build_profile
from user_profile import build_profile as bf
import user_profile as up
from user_profile import*

profile = build_profile(
    'Lee Adonis', 
    'Lucero', 
    location='Philippines', 
    field='Information Technology', 
    hobby='Planting')

user_profile.build_profile(
    'Lee Adonis', 'Lucero', 
    location='Philippines', 
    field='Information Technology', 
    hobby='Planting')

build_profile(
    'Lee Adonis', 
    'Lucero', 
    location='Philippines', 
    field='Information Technology', 
    hobby='Planting')

bf(
    'Lee Adonis', 
    'Lucero', 
    location='Philippines', 
    field='Information Technology', 
    hobby='Planting')

up.build_profile(
    'Lee Adonis', 
    'Lucero', 
    location='Philippines', 
    field='Information Technology', 
    hobby='Planting')

print(profile)