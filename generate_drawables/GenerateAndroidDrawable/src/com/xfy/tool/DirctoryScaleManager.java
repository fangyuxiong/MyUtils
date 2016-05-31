package com.xfy.tool;

import java.io.File;

/**
 * Created by XK on 16/1/15.
 */
public class DirctoryScaleManager {

    private ImageScaleManager imageScaleManager;

    private File dir;

    private String out;

    public DirctoryScaleManager(String srcFile,String outPath){
        File file = new File(srcFile);
        if (file.isDirectory()){
            dir = file;
            out = outPath;
        }else {
            imageScaleManager = new ImageScaleManager(srcFile,outPath);
        }
    }

    public void generateDrawables(){
        if (imageScaleManager != null){
            imageScaleManager.generateDrawables();
        }else {
            generateDrawables(dir);
        }
    }

    private void generateDrawables(File dir){
        if (dir.isDirectory()){
            File[] files = dir.listFiles();
            if (files != null)
                for (File f : files){
                    generateDrawables(f);
                }
        }else {
            if (dir.getName().toLowerCase().endsWith(".png")){
                ImageScaleManager i = new ImageScaleManager(dir.getAbsolutePath(),out);
                i.generateDrawables();
            }
        }
    }
}
