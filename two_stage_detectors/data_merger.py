#!/usr/bin/env python
# coding: utf-8

import os, sys, json
import pandas as pd
annotations_train = pd.read_csv("DLCV_logo_project/annot_train.csv")


exclude = ["Ralph Lauren Corporation","Intimissimi","Chanel","Emirates","Toyota","Pepsi"]
classes = [label for label in annotations_train["class"].unique() if label not in exclude]
#Create final mapping of classes to int
int2str = {k+1:v for k, v in enumerate(classes)}
str2int = {v:k for k, v in int2str.items()}
str2int["Apple Inc-"] = str2int["Apple Inc."]
del str2int["Apple Inc."]

def mergeJson(path, folders):
    #loop through all folders
    for folder in folders:
        path_to_json = path + folder
        i = 0
        new_json = {}
        #check for json files in directory
        for json_file  in os.listdir(path_to_json):
            if json_file.endswith(".json"):  
                print(i)
                final_path = path_to_json + json_file
                
                with open(final_path, "r") as js_file:
                    this_file = json.load(js_file)
             
                if len(new_json) == 0:
                    out_length = 0
                    annot_length = 0
                else: 
                    out_length = len(new_json["images"])
                    annot_length = len(new_json["annotations"])
                #Mapping for changing the annotations
                annot_to_cat = {cat["id"] : cat["name"] for cat in this_file["categories"]}
                
                #mapping of Images
                img_to_new_img = {img["id"] : (img["id"] + out_length) for img in this_file["images"]}
                
                update_img_id(this_file["images"], img_to_new_img)
                change_annotations(this_file["annotations"], annot_to_cat,img_to_new_img,annot_length)
                
                for cat in this_file["categories"][1:]:
                    cat.update({"id":str2int[cat["name"]]})
                    
                
                
                if i == 0: 
                    new_json = this_file
                    
                else: 
                    new_json["images"] += this_file["images"]
                    new_json["annotations"] += this_file["annotations"]
                    new_json["categories"] += this_file["categories"][1:]
                
                i+=1
                print(f"Moving file {final_path}")
                
                os.remove(path_to_json + json_file)
        with open(path_to_json + "_annotateFinal.json","w") as json_file: 
            json.dump(new_json,json_file)
        
    

def change_annotations(annotations, annot_to_cat,img_to_new_img,annot_length):
    for annot in annotations:
        img_id = annot["image_id"]
        annot["id"] += annot_length
        annot.update({"image_id" : img_to_new_img[img_id]})
        annot.update({"category_id" : str2int[annot_to_cat[annot["category_id"]]]})
        

def update_img_id(imgs, img_to_new_img):
    for img in imgs:
        img_id = img["id"]
        img.update({"id" : img_to_new_img[img_id]})



               

if __name__ == "__main__":
    mergeJson("data_COCO/",["train/","test/"])

