package com.minor.startup.controllers;

import javax.servlet.http.HttpServletRequest;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.auth0.AuthenticationController;
import com.minor.startup.security.AppConfig;

@ComponentScan
@Controller
public class LoginController
{
	@Autowired
	private AuthenticationController controller;

	@Autowired
	private AppConfig appConfig;

	private final Logger logger = LoggerFactory.getLogger(this.getClass());

	@RequestMapping(value = "/login")
	protected String login(final HttpServletRequest req)
	{
		String redirectUri = req.getScheme() + "://" + req.getServerName() + ":" + req.getServerPort() + "/callback";
		String authorizeUrl = controller.buildAuthorizeUrl(req, redirectUri)
			.withAudience(String.format("https://%s/userinfo", appConfig.getDomain()))
			.build();
		return "redirect:" + authorizeUrl;
	}

}
