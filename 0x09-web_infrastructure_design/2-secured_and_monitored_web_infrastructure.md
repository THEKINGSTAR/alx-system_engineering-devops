### ```What are firewalls for```
>- A firewall is a division between a private network and an outer network, often the internet, that manages traffic passing between the two networks. It’s implemented through either hardware or software. Firewalls allow, limit, and block network traffic based on preconfigured rules in the hardware or software, analyzing data packets that request entry to the network. In addition to limiting access to computers and networks, a firewall is also useful for allowing remote access to a private network through secure authentication certificates and logins.
>- Firewalls are both networking and security technology. They are often considered the bare minimum and standard for network security. However, they are not the only measure an enterprise takes to secure their network. This firewall analysis describes both the benefits of firewalls and their weaknesses.

### ```Why is the traffic served over HTTPS```
>- With HTTPS if anyone in between the sender and the recipient could open the message, they still could not understand it. Only the sender and the recipient, who know the "code," can decipher the message.
>- Humans could encode their own documents, but computers do it faster and more efficiently. To do this, the computer at each end uses a document called an "SSL Certificate" containing character strings that are the keys to their secret "codes."
>- SSL certificates contain the computer owner's "public key."
>- The owner shares the public key with anyone who needs it. Other users need the public key to encrypt messages to the owner. The owner sends those users the SSL certificate, which contains the public key. The owner does not share the private key with anyone.
>- The security during the transfer is called the Secure Sockets Layer (SSL) and Transport Layer Security (TLS).
>- The procedure for exchanging public keys using SSL Certificate to enable HTTPS, SSL and TLS is called Public Key Infrastructure (PKI).

### ```What monitoring is used for```
>- software monitoring will watch computer metrics, record them, and emit an alert if something is unusual or that could make the computer not work properly happens.
>- You cannot fix or improve what you cannot measure is a famous saying in the tech industry. In the age of the data-ism, monitoring how our software systems are doing is an important thing.

### ```How the monitoring tool is collecting data```
>- Application monitoring: getting data about your running software and making sure it is behaving as expected
>- Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)

### ```Explain what to do if you want to monitor your web server QPS```
>- Use open source solutions, commercial products, cloud-based solutions, log analysis tools, network monitoring tools, and application performance monitoring tools.


### ```Why terminating SSL at the load balancer level is an issue```
>- Data is encrypted from the client to the load balancer but is decrypted at the load balancer, becoming plain text HTTP.
>- It poses a security risk because the data that are passing across the network from the load balancer to the App Server are now unencrypted, and that will leave applications vulnerable to Man-in-the-Middle Attack (MITM).
>- It is quite an expensive job, so terminating SSL at the ELB level will allow your backend instances to focus resources on actually fulfilling the requests, but this will also impact the ELB.
>- It's possible to lose state by doing this - if you have an application running that requires some SSL headers to keep state.
>- You may find that you don't just have to buy more storage nodes when you scale up, you also need to buy a bigger, more powerful, load balancer5.

### ```Why having only one MySQL server capable of accepting writes is an issue```
>- The definition of master-slave replication is that the master handles all writes, and the slave only handles reads, receiving a stream of updates from the master. If both servers handle writes, this falls under the definition of 'master-master replication', which comes with its own host of data consistency issues

### ```Why having servers with all the same components (database, web server and application server) might be a problem```
>- because if one of the servers is compromised, all the servers will be compromised