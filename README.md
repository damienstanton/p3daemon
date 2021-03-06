Python daemonizer class
====================

[![Circle CI](https://circleci.com/gh/damienstanton/p3daemon.svg?style=shield)](https://circleci.com/gh/damienstanton/p3daemon)

This is a Python class that will daemonize your Python script so it can continue running in the background. It works on Unix, Linux and OS X, creates a PID file and has standard commands (start, stop, restart) + a foreground mode.

Based on [python-daemon](https://github.com/serverdensity/python-daemon) by [dmytton](https://github.com/dmytton) which is in turn based on [this original version from jejik.com](http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/).

I have made slight modifications to allow this to work properly in modern versions of Python 3 as well as 2.7. Usage and documentation has not changed otherwise from the original version.

Usage
---------------------

Define a class which inherits from `Daemon` and has a `run()` method (which is what will be called once the daemonization is completed.

	from daemonizer import Daemon
	
	class daemon(Daemon):
		def run(self):
			print("Test Okay")
  

Create a new object of your class, specifying where you want your PID file to exist:
  	
  	daemon_object = daemon("./pid.pid")
  	daemon_object.start()	

Actions
---------------------

* `start()` - starts the daemon (creates PID and daemonizes).
* `stop()` - stops the daemon (stops the child process and removes the PID).
* `restart()` - does `stop()` then `start()`.

Foreground
---------------------

This is useful for debugging because you can start the code without making it a daemon. The running script then depends on the open shell like any normal Python script.

To do this, just call the `run()` method directly.

	daemon_object.run()

Continuous execution
---------------------

The `run()` method will be executed once so if you want the daemon to be doing stuff continuously you may wish to use the [sched][1] module to execute code repeatedly ([example][2]).

Distributed under the `MIT license`

  [1]: http://docs.python.org/library/sched.html
  [2]: https://github.com/boxedice/sd-agent/blob/master/agent.py#L226
