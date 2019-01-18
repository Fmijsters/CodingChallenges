package com.minor.startup.controllers;

import java.io.IOException;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@ComponentScan
@SuppressWarnings("unused")
@Controller
public class ErrorController implements org.springframework.boot.web.servlet.error.ErrorController
{

	private final Logger logger = LoggerFactory.getLogger(this.getClass());

	private static final String PATH = "/error";

	@RequestMapping("/error")
	protected String error(final RedirectAttributes redirectAttributes) throws IOException
	{
		logger.error("Handling error");
		redirectAttributes.addFlashAttribute("error", true);
		return "redirect:/login";
	}

	@Override
	public String getErrorPath()
	{
		return PATH;
	}

}
