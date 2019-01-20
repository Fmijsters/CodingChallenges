package com.minor.startup.controllers;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import java.security.Principal;
import java.util.Map;
@PreAuthorize("hasRole('user')")
@ComponentScan
@RestController
public class HomeController {

    @RequestMapping(value = "/portal/home", method = RequestMethod.GET)
    protected ModelAndView home(final Map<String, Object> model, final Principal principal) {
        if (principal == null) {
            return new ModelAndView("redirect:/logout", model);
        }
        model.put("userId", principal);
        return new ModelAndView("home", model);
    }

    @RequestMapping(value = "/gettext", method = RequestMethod.GET)
    public ResponseEntity<?> getText(final Principal principal) {
        String test_text = "{\"test\":\"Test\"}";
        if (principal == null) {
            System.out.println("yooo");
        } else
            System.out.println(principal);
        return ResponseEntity.ok(test_text);
    }
}
