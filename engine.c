/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   engine.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: youri <youri@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/09 00:00:12 by youri             #+#    #+#             */
/*   Updated: 2026/09/22 19:02:18 by youri            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <string.h>

void try_process_domain(char *cmd, char *domain)
{
    pid_t pid = fork();

    if(pid <= -1)
    {
        write(2, "child creation faild!\n", 22);
        return;
    }
    if(pid == 0)
    {
        execlp(cmd, cmd, domain, NULL);
        perror("exec error");
        return ;
    }
    else
        wait(NULL);
    return;
}
void try_process_domain_op(const char *cmd, char *op, char *domain, char *count)
{
    pid_t pid = fork();
    if(pid <= -1)
    {
        write(2, "child creation faild!\n", 22);
        return ;
    }  
    if (pid == 0)
    {
        execlp(cmd, cmd, op, count, domain, NULL);
        perror("exec faild");
        return;
    }
    else
        wait(NULL);
    return ;
}
void try_process1(const char *cmd, char *IP, char *option, char *count)
{
    pid_t pid = fork();
    
    if(pid < 0)
    {
        write(2, "child creation faild!\n", 22);
        return;
    }
    if(pid == 0)
    {
       execlp(cmd, cmd, option, count, IP, NULL);
       perror("exec faild");
    }
    else
    wait(NULL);
}

int check_domain(char *subd)
{
    if (!subd) return 0;
    
    int count = 0;
    while(*subd)
    {
        if (*subd == '.')
            count++;
        subd++;
    }
    return (count == 4 || count == 0) ? 0 : 1;
}
int check_ip_address(char *ip)
{
    if(!*ip)
        return -1;
    while((*ip >= '0' && *ip <= '9') || *ip == '.')
        ip++;
    if(*ip != '\0')
        return -1;    
    return 1;
}
int check_option(char *op)
{
    if(op[0] != '-')
        return -1;
    op++;
    while(*op && (*op >= '0' && *op <= '9'))   
        op++;
    if(!*op)
        return -1;
    return 1;
}
int check_count(char *count)
{
    return atoi(count);
}
int main(int ac, char **av)
{
    char *cmd = "ping";
    if(ac == 4 && check_domain(av[3]))
    {
        if(check_option(av[1]) == -1)
        {
            printf("Invalid option '%s'\n", av[1]);
            return 0;
        }
        try_process_domain_op(cmd, av[1], av[3], av[2]);
        
    }
    else if(ac == 4)
    {
        if (check_ip_address(av[3]) == -1)
        {
            printf("Invalid ip address '%s'\n", av[3]);
            return 0;
        }
        if(check_option(av[1]) == -1)
        {
            printf("Invalid option '%s'\n", av[1]);
            return 0;
        }
        int count = check_count(av[2]);
        if(count <= 0)
        {   
            printf("[ERROR]: Invalid number of count '%s' must be (1 <= c)\n", av[2]);
            return 0;
        }
        try_process1(cmd, av[3], av[1], av[2]);
    }
    else if(ac == 2 && check_domain(av[1]))
    {
        try_process_domain_op(cmd, "-c", av[1], "5");
        return 0;
    }
    else if(ac == 2 && (strcmp(av[1], "--help") && strcmp(av[1], "-h")))
    {
        if(check_ip_address(av[1]) == -1)
        {
            printf("Invalid ip address '%s'\n", av[1]);
            return 0;
        }
        try_process1(cmd, av[1], "-c", "5");
    }
    else if (ac == 2 && (!strcmp(av[1], "--help") || !strcmp(av[1], "-h")))
    {
        int fd = open("usage.txt", O_RDONLY);
        char c;
        if(fd == -1)
        {
            write(2, "cannot read file!\n", 18);
            return 0;
        }
        while(read(fd, &c, 1) > 0)
            write(1, &c, 1);
    }
    else{
        printf("try: %s --help to see manual!\n", av[0]);
    }
}