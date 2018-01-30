from krgram.tl.base import TLConstructor, TLConstructedType
from krgram.tl.core_types.native import TL_long, TL_int, TL_string
from krgram.tl.core_types.vector import Vector

'''
msgs_ack#62d6b459 msg_ids:Vector<long> = MsgsAck;
'''
class msgs_ack(TLConstructor):
	ID = 0x62d6b459

	def get_structure(self):
		return "msg_ids", Vector(lambda x: TL_long())

class MsgsAck(TLConstructedType):
	CONSTRUCTORS_CLASSES = msgs_ack,

'''
bad_msg_notification#a7eff811 bad_msg_id:long bad_msg_seqno:int error_code:int = BadMsgNotification;
bad_server_salt#edab447b bad_msg_id:long bad_msg_seqno:int error_code:int new_server_salt:long = BadMsgNotification;
'''
class bad_msg_notification(TLConstructor):
	ID = 0xa7eff811

	def get_structure(self):
		return ("bad_msg_id", TL_long()), ("bad_msg_seqno", TL_int()),( "error_code", TL_int())


class bad_server_salt(TLConstructor):
	ID = 0xedab447b

	def get_structure(self):
		return ("bad_msg_id", TL_long()), ("bad_msg_seqno", TL_int()), ("error_code", TL_int()), ("new_server_salt",TL_long())


class BadMsgNotification(TLConstructedType):
	CONSTRUCTORS_CLASSES = bad_msg_notification, bad_server_salt



'''
msgs_state_req#da69fb52 msg_ids:Vector<long> = MsgsStateReq;
msgs_state_info#04deb57d req_msg_id:long info:string = MsgsStateInfo;
msgs_all_info#8cc0d131 msg_ids:Vector<long> info:string = MsgsAllInfo;
'''
class msgs_state_req(TLConstructor):
	ID = 0xda69fb52

	def get_structure(self):
		return "msg_ids", Vector(lambda x: TL_long())


class msgs_state_info(TLConstructor):
	ID = 0x04deb57d

	def get_structure(self):
		return ("req_msg_id", TL_long()), ("info", TL_string())


class msgs_all_info(TLConstructor):
	ID = 0x8cc0d131

	def get_structure(self):
		return ("msg_ids", Vector(lambda x: TL_long())), ("info", TL_string())

#############

'''
msg_detailed_info#276d3ec6 msg_id:long answer_msg_id:long bytes:int status:int = MsgDetailedInfo;
msg_new_detailed_info#809db6df answer_msg_id:long bytes:int status:int = MsgDetailedInfo;

msg_resend_req#7d861a08 msg_ids:Vector<long> = MsgResendReq;

//rpc_result#f35c6d01 req_msg_id:long result:Object = RpcResult; // parsed manually

rpc_error#2144ca19 error_code:int error_message:string = RpcError;

rpc_answer_unknown#5e2ad36e = RpcDropAnswer;
rpc_answer_dropped_running#cd78e586 = RpcDropAnswer;
rpc_answer_dropped#a43ad8b7 msg_id:long seq_no:int bytes:int = RpcDropAnswer;

future_salt#0949d9dc valid_since:int valid_until:int salt:long = FutureSalt;
future_salts#ae500895 req_msg_id:long now:int salts:vector<future_salt> = FutureSalts;

pong#347773c5 msg_id:long ping_id:long = Pong;

destroy_session_ok#e22045fc session_id:long = DestroySessionRes;
destroy_session_none#62d350c9 session_id:long = DestroySessionRes;

new_session_created#9ec20908 first_msg_id:long unique_id:long server_salt:long = NewSession;

//message msg_id:long seqno:int bytes:int body:Object = Message; // parsed manually
//msg_container#73f1f8dc messages:vector<message> = MessageContainer; // parsed manually
//msg_copy#e06046b2 orig_message:Message = MessageCopy; // parsed manually, not used - use msg_container
//gzip_packed#3072cfa1 packed_data:string = Object; // parsed manually

http_wait#9299359f max_delay:int wait_after:int max_wait:int = HttpWait;

ipPort ipv4:int port:int = IpPort;
help.configSimple#d997c3c5 date:int expires:int dc_id:int ip_port_list:Vector<ipPort> = help.ConfigSimple;

---functions---

rpc_drop_answer#58e4a740 req_msg_id:long = RpcDropAnswer;

get_future_salts#b921bd04 num:int = FutureSalts;

ping#7abe77ec ping_id:long = Pong;
ping_delay_disconnect#f3427b8c ping_id:long disconnect_delay:int = Pong;

destroy_session#e7512126 session_id:long = DestroySessionRes;

contest.saveDeveloperInfo#9a5f6e95 vk_id:int name:string phone_number:string age:int city:string = Bool;
'''