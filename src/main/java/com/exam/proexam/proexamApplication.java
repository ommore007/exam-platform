package com.exam.proexam;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ProexamApplication {

    public static void main(String[] args) {
        SpringApplication.run(ProexamApplication.class, args);
        System.out.println("✅ Server Started at http://localhost:8080");
    }

}
