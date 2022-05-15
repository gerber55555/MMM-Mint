
/* Magic Mirror
 * Module: MMM-Mint
 *
 * By Christian Gerber
 *
 */

var NodeHelper = require("node_helper");

module.exports = NodeHelper.create({

    start: function () {
        console.log('MMM-Mint helper, started...');
    },

    getMintData: function() {
        var self = this;
        const { spawn } = require('child_process');
        var process = spawn("python3", ["/home/pi/MagicMirror/modules/MMM-Mint/mint.py"]);
        process.stdout.on('data', function(data)
        {
            console.log(String.fromCharCode(...data))
            self.sendSocketNotification('GOT-MINT-DATA', String.fromCharCode(...data))
        })
    },
    

    socketNotificationReceived: function(notification, payload) {
        if(notification === 'GET-MINT-DATA') {
            this.getMintData()
        }
    }
})