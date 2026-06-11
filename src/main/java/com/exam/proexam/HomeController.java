package com.exam.proexam;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    @GetMapping("/")
    public String home(Model model) {
        model.addAttribute("categories", new String[]{"पोलिस", "आर्मी", "तलाठी", "SSC", "रेल्वे"});
        model.addAttribute("years", new String[]{"2021", "2022", "2023", "2024", "2025", "2026"});
        return "index";
    }

}
