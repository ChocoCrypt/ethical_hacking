import frida

def on_message(meessage, data):
    print("[on_message] meessage: " , message , "data : ", data)

session = frida.attach("gedit")

script = session.create_script("""
rpc.exports.enumerateModules = function(){
    return Process.enumerateModules();
};
""")
script.on("message " , on_message)
script.load()

print([m["name"]for m in script.exports.enumerate_modules()])
# print([m["name"] for m in script.exports.enumerate_modules()])
