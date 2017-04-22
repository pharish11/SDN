
from mininet.topo import Topo
class MyTopo( Topo ):
    "Simple topology example."
    def __init__( self ):
        "Create custom topo."
        # Initialize topology
        Topo.__init__( self )
        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        # Add links
        self.addLink( h1, s1 )
        self.addLink( h2, s1 )
        self.addLink( h3, s1 )
        self.addLink( s1, s2 )
        self.addLink( s2, h4 )
        topos = { 'mytopo': ( lambda: MyTopo() ) }
        lab5.py from pox.core import core
        import pox.openflow.libopenflow_01 as of
        from pox.lib.util import dpidToStr
        log = core.getLogger()
        s1_dpid=0
        s2_dpid=0
        def _handle_ConnectionUp (event):
            global s1_dpid, s2_dpid
            print "ConnectionUp: ",
            dpidToStr(event.connection.dpid)
            #remember the connection dpid for switch
            for m in event.connection.features.ports:
                if m.name == "s1-eth1":
                    s1_dpid = event.connection.dpid
                    print "s1_dpid=", s1_dpid
                elif m.name == "s2-eth1":
                    s2_dpid = event.connection.dpid
                    print "s2_dpid=", s2_dpid
