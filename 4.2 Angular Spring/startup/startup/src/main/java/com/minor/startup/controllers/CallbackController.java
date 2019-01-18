package com.minor.startup.controllers;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.http.MediaType;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.auth0.AuthenticationController;
import com.auth0.IdentityVerificationException;
import com.auth0.Tokens;
import com.auth0.jwt.JWT;
import com.minor.startup.security.TokenAuthentication;

@ComponentScan
@Controller
public class CallbackController
{
	@Autowired
	private AuthenticationController controller;

	private final String redirectOnFail;

	private final String redirectOnSuccess;

	public CallbackController()
	{
		this.redirectOnFail = "/login";
		this.redirectOnSuccess = "/portal/home";
	}

	@RequestMapping(value = "/callback", method = RequestMethod.GET)
	protected void getCallback(final HttpServletRequest req, final HttpServletResponse res) throws ServletException, IOException
	{
		handle(req, res);
	}

	@RequestMapping(value = "/callback", method = RequestMethod.POST, consumes = MediaType.APPLICATION_FORM_URLENCODED_VALUE)
	protected void postCallback(final HttpServletRequest req, final HttpServletResponse res) throws ServletException, IOException
	{
		handle(req, res);
	}

	private void handle(HttpServletRequest req, HttpServletResponse res) throws IOException
	{
		try
		{
			Tokens tokens = controller.handle(req);
			TokenAuthentication tokenAuth = new TokenAuthentication(JWT.decode(tokens.getIdToken()));
			SecurityContextHolder.getContext().setAuthentication(tokenAuth);
			res.sendRedirect(redirectOnSuccess);
		}
		catch (AuthenticationException | IdentityVerificationException e)
		{
			e.printStackTrace();
			SecurityContextHolder.clearContext();
			res.sendRedirect(redirectOnFail);
		}
	}
}
