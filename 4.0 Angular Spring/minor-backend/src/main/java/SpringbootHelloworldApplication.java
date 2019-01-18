package com.startup.springboothelloworld;

import com.startup.springboothelloworld.dao.daointerface.GebruikerDao;
import com.startup.springboothelloworld.model.Gebruiker;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.context.annotation.Bean;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.javamail.JavaMailSenderImpl;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;

import java.util.Properties;


@EntityScan
@SpringBootApplication
public class SpringbootHelloworldApplication {
    private static InMemoryUserDetailsManager inMemoryUserDetailsManager;

    @Autowired
    public SpringbootHelloworldApplication(InMemoryUserDetailsManager inMemoryUserDetailsManager) {
        SpringbootHelloworldApplication.inMemoryUserDetailsManager = inMemoryUserDetailsManager;
    }


    public static void main(String[] args) {
        SpringApplication app = new SpringApplication(SpringbootHelloworldApplication.class);
        app.run(args);
        initUsers();
    }

    private static void initUsers() {
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        GebruikerDao gebruikerDao = context.getBean(GebruikerDao.class);
        for (Object object : gebruikerDao.getAsList()) {
            Gebruiker gebruiker = (Gebruiker) object;
            inMemoryUserDetailsManager.createUser(gebruiker.gebruikerToUserDetails());
        }
    }

    @Bean
    public JavaMailSender getJavaMailSender() {
        JavaMailSenderImpl mailSender = new JavaMailSenderImpl();
        mailSender.setHost("smtp.gmail.com");
        mailSender.setPort(587);

        mailSender.setUsername("startupplannersaxion@gmail.com");
        mailSender.setPassword("startupplanner");

        Properties props = mailSender.getJavaMailProperties();
        props.put("mail.transport.protocol", "smtp");
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.starttls.enable", "true");
        props.put("mail.debug", "true");

        return mailSender;
    }
}

