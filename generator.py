import os
import shutil

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_file(path, content):
    # Ensure the directory exists before creating the file
    directory = os.path.dirname(path)
    create_directory(directory)
    
    with open(path, 'w') as file:
        file.write(content)

def create_spring_boot_project(project_name, package_name):
    base_dir = project_name
    src_dir = os.path.join(base_dir, "src", "main", "java", package_name.replace(".", os.sep))
    resources_dir = os.path.join(base_dir, "src", "main", "resources")

    create_directory(src_dir)
    create_directory(resources_dir)

    # Create pom.xml
    pom_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.5.5</version>
        <relativePath/>
    </parent>
    <groupId>{package_name}</groupId>
    <artifactId>{project_name}</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>{project_name}</name>
    <description>Demo project for Spring Boot</description>
    <properties>
        <java.version>11</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
"""
    create_file(os.path.join(base_dir, "pom.xml"), pom_content)

    # Create main application class
    main_class_content = f"""package {package_name};

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class {project_name.capitalize()}Application {{

    public static void main(String[] args) {{
        SpringApplication.run({project_name.capitalize()}Application.class, args);
    }}

}}
"""
    create_file(os.path.join(src_dir, f"{project_name.capitalize()}Application.java"), main_class_content)

    # Create a sample REST controller
    controller_content = f"""package {package_name}.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {{

    @GetMapping("/hello")
    public String hello() {{
        return "Hello, World!";
    }}

}}
"""
    create_file(os.path.join(src_dir, "controller", "HelloController.java"), controller_content)

    # Create application.properties
    create_file(os.path.join(resources_dir, "application.properties"), "server.port=8080")

    print(f"Spring Boot project '{project_name}' created successfully!")

# Example usage
project_name = input("Enter project name: ")
package_name = input("Enter package name: ")
create_spring_boot_project(project_name, package_name)
