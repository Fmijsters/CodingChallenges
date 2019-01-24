package com.minor.startup.filter;

import com.auth0.jwt.JWT;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.filter.GenericFilterBean;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletRequest;
import java.io.IOException;

public class AuthenticationFilter extends GenericFilterBean {

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) {
        if (((HttpServletRequest) request).getHeader("authorization") != null) {
            TokenAuthentication tokenAuth = new TokenAuthentication(JWT.decode(((HttpServletRequest) request).getHeader("authorization")));
            SecurityContextHolder.getContext().setAuthentication(tokenAuth);
        }
        try {
            chain.doFilter(request, response);
        } catch (IOException | ServletException e) {
            e.printStackTrace();
        }


    }
}
