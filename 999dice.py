B
    6]�3  �            	   @   sL  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlmZm	Z	m
Z
 d dlmZ d dlmZ ejdd� ejdd�Zejd	d
d dd� e�� Zedd��Ze�� ZW dQ R X e�e�Zee
jej d e
j ej d e
j ej d e
j ej d e
j  d e
j ej d e
j ej d e
j  d e
j ej d e
j ej d e
j ej! d e
j ej d e
j ej d e
j ej d e
j ej d e
j ej d e
j ej d e
j  d e
j ej d  e
j  d! e
j ej d" e
j  d# � e
jej Z"e
j Z#e
jej Z$e
jej Z%e
jej Z&e
jej! Z'e
jej! Z(e �)� Z*d$Z+d%ed& d'd(d)d*d+�Z,d,d-� Z-d.d/� Z.d0d1� Z/e*j0e+e,d2d3ed4 d5 ed4 d6 d7d8�d9�Z1e�e1j2�Z3y4ee"d: e$ d e# e4e5e3d; d< �d= � � W n   ed>� e�6�  Y nX e/e7e5ed? �d= �e7e5ed@ �d= �� dS )A�    N)�Fore�Back�Style)�randint)�datetimeT)Z	autoresetz<999 Dice Bot | This Is Gambling Bot Plase Take Own Your Risk)�descriptionz-cz--betsetz%Enter Your Betset Number (default: 0))�default�helpzconfig.json�rz�      ___  _           ___       __
     / _ \(_)______   / _ )___  / /_
    / // / / __/ -_) / _  / _ \/ __/
   /____/_/\__/\__/ /____/\___/\__/z)
=======================================
zAuthor By  z: zKadal15
zChannel Yt �:z Jejaka Tutorialz
999 Dice Botz | zLose Streak �|z Win Streak
z:support by botakberambut(hijrah) And All Termux Id Member
zDonate z BTC z#18961sqv9fPuBcEbbi1gHub8ydWePB8yaG
z         LTC z#LNRkk6o9h1Rh98sDW8byeH9HbeUHwNohDu
z         Doge z$DJG4YG3ARUkSt9e5xvHvSS3faVx3v1HM9p

z$https://www.999doge.com/api/web.aspxzfile://z
User-Agentz!application/x-www-form-urlencodedz*/*z#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7zcom.reland.relandicebot)ZOriginz
user-agentzContent-typeZAcceptzAccept-LanguagezX-Requested-Withc             C   s�   t dt| � d �}|dks,|dks,|dkrbt |�d�d �}dt|� }tt|�d	|  �ada|d
ks�|dks�|dks�|dks�|dkr�dat|�d�d �ad S )Ni?B �d   �Hi�hiZHI�.�   �   �
   �LoZLOW�low�LowZLOr   )�str�float�split�len�intr   �high)ZpersenZtaruhan�c�nZpangkat� r   �dice.py�konvert2   s    (r!   c             C   s�   t | �dk r4tdt | � �}|d t| � } d|  }t | �dkrjtdt | � �}|d t| � } d|  }n0t | �}| dd � }| d |d � }|d | }|S )N�   �0z0.i����r   )r   r   r   )�numZpanjang_nol�resultZlen_num�end�firstr   r   r    �rev@   s    
r(   c       %      C   sr  t jdkst jdkst jdkrZd}d}x<|d7 }ytd | d }W q(   P Y q(X q(W n
tt j�}ttd | d �d	 }ttd | d
 �d }tttd | d �d �}ttd | d td | d d � |}dtd |ttt	dd�ddd�}	�y�t
jtt|	d�}
t�|
j�}|d t|d � t|� }t|d �t|� }t|d t|d � t|� | �d }ttd tttt|d �t|� �d � � tdtd | d  � d}d}d}d}t�� �d�}t|�ttd � }d}d}d}d}d}d}td | d }td | d }�
x�|dk�sD|dk�sD|d k�rJd}nd!}td | d" dk�s�td | d" d k�s�td | d" dk�r�tj�d#� n&|tttd | d" �d �k�r�|}td | d d$ d% d&k�std | d d$ d% d'k�std | d d$ d% d(k�r�|d7 }|d!k�r�|ttd | d d$ d) �d k�rZd*}|ttd | d d$ d) �d+ d k�r�d}d}|d!k�r|ttd | d d$ d, �d k�r�d*}|ttd | d d$ d, �d+ d k�rd}d}ntd | d d }t jdk�s,t jdk�s,t jdk�r�t�� �d�}t|�t|d �k�r�t|�ttd � }|d7 }||k�rzd}td-td | d  d. � ttd | d �d	 }ttd | d
 �d }tttd | d �d �}|}n
tt j�}td | d/ d% d'k�s@td | d/ d% d&k�s@td | d/ d% d(k�r�tt�ttd | d/ d0 �ttd | d/ d1 ��d+�}tt|��}|d2k�r�tj�d3t|� d4 � |d5k�r�tj�d3t|� d6 � |d7k�r�tj�d3t|� d8 � t|t|�� nttd | d t|�� t� t|�� t|�}|d7 }dtd |ttt	dd�ddd�}	|ttd9 �k�r�ttd: t d; t t|� � t!�"d<t|� � t� d� t!�"d=ttt|d �t|� �d � � t�#�  t
jtt|	d�}
t�|
j�}t|d t|d � t|� | �d }t|d �t|� }|d | k�r�tt$d> t t|� t$ d? t% tt|�d � tttt|d �t|� �d � t%d@ tt|� � ttdA � t!�"dB� t� d� t!�"d=ttt|d �t|� �d � � t�#�  |d |k �r�tt$d> t t|� t$ dC t& dD tt|�d � tttt|d �t|� �d � t&dE tt|� � tt'j(t)j* dF � t!�"dG� t� d� t!�"d=ttt|d �t|� �d � � t�#�  |d dk	�	r�|d7 }d}t|d �t|� } |dk�	rTtt$d> t t|� t$ d? t% tt+t|��� ttt+t| ��� t%d@ tt|� � nVtt$d> t t|� t$ d? t% tt+t|��� ttt+t| ��� t&dE tt|� � t|�ttd | d) � }�nd}|d7 }d}!d!}t|d �t|� } |dk�
rXtt$d> t t|� t$ dC t& dD tt+t|��� ttt+t| ��� t%d@ tt|� � nZtt$d> t t|� t$ dC t& dD tt+t|��� ttt+t| ��� t&dE tt|� � t|�ttd | d, � }|d!k�
r�|!d7 }!|!|k�r4d}!d}n@||k�r4d}|d!k�r0|t|�k�r4|}t|�t|� }n|}||k�rNd!}d}|d7 }||k�rhd!}d}|d7 }tj�tdH t t|� t, dI t t|� d3 � tdJ d% d&k�s�tdJ d% d'k�s�tdJ d% d(k�r&tt+t| ���ttdJ dK �k�r&dLtd tttdJ dM �d �tdJ dN d#ddO�}"t
jtt|"d�}
t�|
j�}#td#� tdPtt+t|#dQ ��� � t-dRdS��(}$|$�dPtt+t|#dQ ��� dT � W d Q R X t�#�  �q&W W n�   td#� t!�"dU� y~t-dRdS��j}$|$�d>t�� �dV� dW t|� dI t|� dX ttt|d �t|� �d � dY t|� dT � W d Q R X W n   tt&dZ � Y nX t�#�  Y nX d S )[NZAuto�autoZAUTOr   r   ZConfigzName Bet SetZIntervali�  zReset If WinzBase Beti ��ZChanceZBetZPlaceBetZSessionCookiei?B Zdoge�2)�a�sZPayInr   ZHighZ
ClientSeed�CurrencyZProtocolVersion)�headers�dataZStartingBalanceZPayOutz


Starting BalancezAnda Menggunakan BetSet Ke Fz%Mr   zReset If ProfitZOFFZOffZoffTzMax Bet� zHi / LowZToggleZOnZON�onzIf Winr   �   zIf LosezChange Bet Set z                           zRandom ChanceZMinZMax�   �z   �   z  �   � zTarget Profitz%
Yay.! 
Profit Mencapai Target.....!
zProfit ztermux-toast You win ztermux-toast Total Balance �[z] ZProfitz)Yay.!
Balance Sudah Memenuhi Target.....!z&termux-toast Target Win Sudah Tercapai�]�-zLose zLose Target....!ztermux-toast Lose Target z        Win Streak z Lose Streak zAuto Wdz
If BalanceZWithdraw�AmountzWallet Address)r+   r,   r;   ZAddress�Totpr-   z	Withdraw ZPendingzhistory.logza+�
ztermux-toast Betting Stopz%Y/%m/%d %H:%M:%Sz] Win Streak z | Balance z Profit z%Balance Tidak Mencukupi Untuk Betting).�my_namespaceZbetset�objr   r   r!   �jsr   r   r   r   Zpost�url�ua�json�loads�text�print�hijau�resr   r   �now�strftime�sys�stdout�write�round�random�uniformr   �time�sleep�os�system�exit�ungu�hijau2�red2r   �BRIGHTr   �REDr(   �red�open)%ZwsZlsZurutZjumlahulangZpesanZslpZlimit_aZpayinZamountr/   Zr1ZjsnZjumblZjumZprofr   ZburstZstats_rolebet_loseZstats_rolebet_winZmenitZno_winZno_loseZ	total_winZ
total_loseZ
no_rolebetZrolebetZreset_if_profitZtot_if_profitZstats_if_profitZwaktuZhasil_chanceZcokZbal�iZwdZwithdraw�fr   r   r    �diceR   sz   
&(.B"Z
&*
&*$

N:


 
*(f

*j

*
XV 
\Z





46"
,
rr_   ZLoginZ 7ec7f8a2c9724b2cbb8ed75e72b47ee9ZAccount�Username�Passwordr0   )r+   ZKeyr`   ra   r<   )r.   r/   zBalance ZDogeZBalancei ��z%Check Your Username And Your Passwordz
Target WinzLose Target)8ZrequestsrC   rQ   rK   rO   rS   �argparseZcoloramar   r   r   r   r   �init�ArgumentParser�parser�add_argument�
parse_argsr>   r\   Zmyfile�readr/   rD   r?   rF   ZNORMALZMAGENTAZGREENrY   ZDIMZWHITEZ	RESET_ALLrZ   rG   rH   Zabu2rV   rW   rX   r[   Zsessionr   rA   rB   r!   r(   r_   �getr
   rE   r@   r   r   rU   r   r   r   r   r    �<module>   sV   8
� G Z,4