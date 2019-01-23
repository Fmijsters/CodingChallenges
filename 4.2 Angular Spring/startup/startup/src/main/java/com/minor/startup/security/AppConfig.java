package com.minor.startup.security;

import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.config.http.SessionCreationPolicy;

@Configuration
@EnableWebSecurity
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class AppConfig extends WebSecurityConfigurerAdapter
{

	@Override
	protected void configure(HttpSecurity http) throws Exception
	{
		http.csrf().disable();
		http
			.authorizeRequests()
			.antMatchers("/v2/api-docs").permitAll()
			.antMatchers("/**").authenticated()
			.and()
			.logout().permitAll();
		http.sessionManagement().sessionCreationPolicy(SessionCreationPolicy.NEVER);
	}
}