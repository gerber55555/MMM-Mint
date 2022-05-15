Module.register("MMM-Mint", {
    
    defaults: {
        // Intervals
        animationSpeed: 1,   // 1 sec.
        updateInterval: 3600, // 60 min.

        // Style
        maxWidth: '400px',
        textSize: 'medium',
    },

    getTemplate: function() {
        return 'MMM-Mint.njk';
    },

    getTemplateData: function() {
        return {
            config: this.config,
            mintData: this.mintData,
        };
    },

    getHeader: function() {
        return "Mint Data"
    },

    getStyles() {
        return ["MMM-Mint.css"]
    },

    start: function() {
        Log.log('Starting module: ' + this.name);

        this.loaded = false;

        this.mintData = null;

        this.getMintData(this)
        
        setInterval(() => {
            this.getMintData(this) 
        }, this.config.updateInterval * 1000)

    },

    getMintData: function(_this) {
        Log.log('Fetching Mint Data...');
        _this.sendSocketNotification('GET-MINT-DATA', null);
    },

    socketNotificationReceived: function(notification, payload) {
        if(notification === 'GOT-MINT-DATA') {
            Log.log("Got Mint Data")
            this.loaded = true;
            this.mintData = JSON.parse(payload);
            Log.log(this.mintData)
            this.updateDom(this.animationSpeed * 1000)
        }
    }
});