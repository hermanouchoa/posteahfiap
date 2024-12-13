
/*SELECT   b.valor,   b.descricao_valor
FROM `quantum-device-443518-b1.pnad_covid.dominio` a inner join 
     `quantum-device-443518-b1.pnad_covid.valores` b on
     a.codigo = b.cod_tabela
where a.codigo = 'UF'
and b.valor = '15'*/

SELECT b.descricao_valor
FROM `quantum-device-443518-b1.pnad_covid.dominio` a inner join 
     `quantum-device-443518-b1.pnad_covid.valores` b on
     a.codigo = b.cod_tabela
where a.codigo = 'UF' and b.valor = '15'
