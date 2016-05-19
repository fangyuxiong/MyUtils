package com.xfy.tool;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

/**
 * Created by XK on 16/1/15.
 */
public class FileUtil {

    private File outPath;

    private String fileName;

    public FileUtil(String name,File output){
        fileName = name;
        outPath = output;
    }

    public void save(Image image,ScareType type){
        int w = image.getWidth(null);
        int h = image.getHeight(null);
        BufferedImage bi = new BufferedImage(w,h,BufferedImage.TYPE_4BYTE_ABGR);
        Graphics g = bi.getGraphics();
        g.drawImage(image,0,0,null);

        try {
            ImageIO.write(bi,"png",getOutPath(type));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String getFileName(){
        return fileName;
    }

    public File getOutPath(){
        return outPath;
    }

    public String getOutPathBy(ScareType type){
        return outPath.getAbsolutePath() + "/drawable-" + type.toString();
    }

    private File getOutPath(ScareType type){
        if (!outPath.exists()){
            outPath.mkdirs();
        }
        File file = new File(outPath,"drawable-"+type.toString());
        if (!file.exists())
            file.mkdirs();
        return new File(file,fileName);
    }
}
