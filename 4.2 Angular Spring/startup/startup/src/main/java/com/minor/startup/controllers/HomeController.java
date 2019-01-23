package com.minor.startup.controllers;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@ComponentScan
@RestController
public class HomeController
{
	@RequestMapping(value = "/gettext", method = RequestMethod.GET)
	public ResponseEntity<?> getText()
	{
		String test_text = "{\"test\":\"Test\"}";
		return ResponseEntity.ok(test_text);
	}
}
