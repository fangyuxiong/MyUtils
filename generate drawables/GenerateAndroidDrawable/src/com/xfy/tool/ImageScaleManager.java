package com.xfy.tool;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.channels.FileChannel;

/**
 * Created by XK on 16/1/15.
 */
public class ImageScaleManager {

    private ImageScaleUtil imageScaleUtil;

    private FileUtil fileUtil;

    public ImageScaleManager(String srcFile,String outPath){
        this(srcFile,outPath,null);
    }

    public ImageScaleManager(String srcFile,String outPath,String name){
        File src = new File(srcFile);
        imageScaleUtil = new ImageScaleUtil(src);

        fileUtil = new FileUtil(name == null ? src.getName() : name,new File(outPath));
    }

    public void generateDrawables(){
        print("start generate " + fileUtil.getFileName());

        for (ScareType t : ScareType.values()){
            fileUtil.save(imageScaleUtil.generateImage(t),t);
        }

        File dF = new File(fileUtil.getOutPath().getAbsoluteFile() + "/drawable");
        if (!dF.exists())
            dF.mkdirs();

        fileChannelCopy(
                new File(fileUtil.getOutPathBy(ScareType.MDPI),fileUtil.getFileName())
                ,new File(dF , fileUtil.getFileName() ));

        print("generate success");
    }

    private void print(String s){
        System.out.println(s);
    }

    private void fileChannelCopy(File s, File t) {

        FileInputStream fi = null;

        FileOutputStream fo = null;

        FileChannel in = null;

        FileChannel out = null;

        try {

            fi = new FileInputStream(s);

            fo = new FileOutputStream(t);

            in = fi.getChannel();//得到对应的文件通道

            out = fo.getChannel();//得到对应的文件通道

            in.transferTo(0, in.size(), out);//连接两个通道，并且从in通道读取，然后写入out通道

        } catch (IOException e) {

            e.printStackTrace();

        } finally {

            try {

                fi.close();

                in.close();

                fo.close();

                out.close();

            } catch (Exception e) {

                e.printStackTrace();

            }

        }

    }
}
