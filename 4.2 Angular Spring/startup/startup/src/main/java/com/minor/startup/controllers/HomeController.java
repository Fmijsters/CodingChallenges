package com.minor.startup.controllers;

import java.security.Principal;
import java.util.Map;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@ComponentScan
@Controller
public class HomeController
{

	@RequestMapping(value = "/portal/home")
	protected String home(final Map<String, Object> model, final Principal principal)
	{
		if (principal == null)
		{
			return "redirect:/logout";
		}
		model.put("userId", principal);
		return "home";
	}
}
