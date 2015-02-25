#!/usr/bin/env python
 
import sys
 
class MessagesXmlParser():
        def __init__(self, filename):
                import xml.etree.ElementTree as etree
 
                self.keys = []
 
                tree = etree.parse(filename)
                root = tree.getroot()
                for message in root:
                        self.keys.append(message.attrib['key'])
 
class MessagesPropertiesParser():
        def __init__(self, filename):
                try:
                        import jprops
                except:
                        print('Error: jprops module for parsing .properties files is missing. Download and follow installation instructions from http://mgood.github.com/jprops/')
                        sys.exit(2)
 
                self.keys = []
 
                with open(filename) as fp:
                        for key, value in jprops.iter_properties(fp):
                                self.keys.append(key)
 
if __name__ == "__main__":
        if len(sys.argv) != 3:
                print("Usage:")
                print("       %s messages.xml messages_XX.xml" % (sys.argv[0]))
                print("or")
                print("       %s Messages.properties Messages_XX.properties" % (sys.argv[0]))
                sys.exit(1)
 
        testfile = open(sys.argv[1], 'rb')
        if testfile.readline().find('<?xml') != -1:
                # xml file detected, assume messages.xml
                messages_tmpl = MessagesXmlParser(sys.argv[1])
                messages_in   = MessagesXmlParser(sys.argv[2])
        else:
                # assume Messages.properties
                messages_tmpl = MessagesPropertiesParser(sys.argv[1])
                messages_in   = MessagesPropertiesParser(sys.argv[2])
 
        print "Present in %s but missing in %s:" % (sys.argv[1], sys.argv[2])
        for i in set(messages_tmpl.keys) - set(messages_in.keys):
                print i
        print "\nPresent in %s but missing in %s:" % (sys.argv[2], sys.argv[1])
        for i in set(messages_in.keys) - set(messages_tmpl.keys):
                print i
 
