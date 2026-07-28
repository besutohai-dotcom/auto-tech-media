# -*- coding: utf-8 -*-
import os
import shutil
import glob

BRAIN_DIR = "/Users/kaibest/.gemini/antigravity/brain/46787952-97fc-4073-837c-f0af285da40d"
ASSETS_DIR = "/Users/kaibest/.gemini/antigravity/scratch/auto_blogger/dist/assets"

os.makedirs(ASSETS_DIR, exist_ok=True)

hero_files = glob.glob(os.path.join(BRAIN_DIR, "ai_hero_cover_*.jpg"))
brain_files = glob.glob(os.path.join(BRAIN_DIR, "ai_brain_cover_*.jpg"))

if hero_files:
    shutil.copy(hero_files[0], os.path.join(ASSETS_DIR, "hero.jpg"))
    print(f"Copied hero image: {hero_files[0]}")

if brain_files:
    shutil.copy(brain_files[0], os.path.join(ASSETS_DIR, "brain.jpg"))
    print(f"Copied brain image: {brain_files[0]}")
