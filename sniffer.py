from burp import IBurpExtender, IHttpListener, IMessageEditorController
from java.io import PrintWriter
import re

class BurpExtender(IBurpExtender, IHttpListener):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        self._stdout = PrintWriter(callbacks.getStdout(), True)
        self._stderr = PrintWriter(callbacks.getStderr(), True)

        callbacks.setExtensionName("AuthSniffer")
        callbacks.registerHttpListener(self)

        self._stdout.println("AuthSniffer foi carregado e está farejando tokens...")

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if messageIsRequest:
            content = messageInfo.getRequest()
        else:
            content = messageInfo.getResponse()

        if content is None:
            return

        analyzed = self._helpers.analyzeRequest(content) if messageIsRequest else self._helpers.analyzeResponse(content)
        body_offset = analyzed.getBodyOffset()
        content_bytes = content[body_offset:]
        content_str = self._helpers.bytesToString(content_bytes)

        tokens = self.sniff_tokens(content_str)
        if tokens:
            self._stdout.println("=== Tokens Encontrados ===")
            for t in tokens:
                self._stdout.println(t)
            self._stdout.println("==========================")

    def sniff_tokens(self, text):
        patterns = [
            r"Bearer\s+[A-Za-z0-9\-\._~\+\/]+=*",
            r"eyJ[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+",  # JWT
            r"api[_-]?key\s*[=:]\s*[A-Za-z0-9\-\._~\+\/]+",
            r"Authorization:\s*Basic\s+[A-Za-z0-9\+/=]+"
        ]
        found = []
        for p in patterns:
            found += re.findall(p, text)
        return found
