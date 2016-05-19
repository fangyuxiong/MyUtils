package com.xfy.tool;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
	// write your code here
        print("args length:"+(args != null ? args.length + (args.length == 2 ? " src:"+args[0] +" out:"+args[1] : Arrays.toString(args)): "-1"));
        if (args != null && args.length == 2){

            DirctoryScaleManager manager = new DirctoryScaleManager(args[0],args[1]);
            manager.generateDrawables();

        }else {
            print("param wrong");
        }

    }

    static void print(String s){
        System.out.println(s);
    }
}
